import inspect
from typing import Callable, List, Dict, Optional


class Pipeline:
    def __init__(self):
        self._committed: List[Dict] = []
        self._compiled: bool = False
        self._imports = set()


    def commit(
        self,
        func: Callable = None,
        inputs: Optional[List[str]] = None,
        outputs: Optional[List[str]] = None,
        stage: Optional[str] = None,
        mode: Optional[str] = None,
    ):
        
        # Semi-auto commit mode
        
        if mode == "functions":
            import inspect

            caller_globals = inspect.currentframe().f_back.f_globals
            new_functions = []

            for name, obj in caller_globals.items():

                if not inspect.isfunction(obj):
                    continue

                if not hasattr(obj, "__code__"):
                    continue

                # Must belong to caller's module
                if obj.__module__ != caller_globals.get("__name__"):
                    continue

                # Skip private
                if name.startswith("_"):
                    continue

                # Ensure top-level only
                if obj.__qualname__ != obj.__name__:
                    continue

                # Skip already committed
                if any(entry["func"] == obj for entry in self._committed):
                    continue

                new_functions.append(obj)

            if not new_functions:
                print("[QuickLearn] ⚠ No new top-level functions found.")
                return

            for fn in new_functions:
                self._committed.append({
                    "func": fn,
                    "inputs": [],
                    "outputs": [],
                    "stage": stage or "General"
                })
                print(f"[QuickLearn] ✅ Auto-committed: {fn.__name__}")

            return

        if self._compiled:
            raise RuntimeError("Pipeline already compiled. Reset before committing again.")

        if not callable(func):
            raise TypeError("commit() expects a callable function.")
        
        # Guard: func must be provided in manual mode
        if func is None:
            raise ValueError("commit() requires a function unless mode='functions' is used.")

        # Guard: block lambdas
        if func.__name__ == "<lambda>":
            raise ValueError("Cannot commit lambda functions.")

        # Guard: only allow top-level functions
        if func.__qualname__ != func.__name__:
            raise ValueError("Only top-level functions can be committed.")

        # Guard: must be user-defined Python function (not builtin)
        if not hasattr(func, "__code__"):
            raise ValueError("Only user-defined Python functions can be committed.")

        
        for entry in self._committed:
            if entry["func"] == func:
                # Update metadata instead of skipping
                if inputs is not None:
                    entry["inputs"] = inputs
                if outputs is not None:
                    entry["outputs"] = outputs
                if stage is not None:
                    entry["stage"] = stage

                print(f"[QuickLearn] 🔄 Updated metadata for: {func.__name__}")
                return

        self._committed.append({
            "func": func,
            "inputs": inputs or [],
            "outputs": outputs or [],
            "stage": stage or "General"
        })

        print(f"[QuickLearn] ✅ Committed: {func.__name__}")

    def summary(self):
        if not self._committed:
            print("[QuickLearn] No committed functions.")
            return

        print("\n[QuickLearn] 📦 Pipeline Summary\n")

        for i, entry in enumerate(self._committed, start=1):
            print(f"{i}. {entry['func'].__name__}")
            print(f"   Stage: {entry['stage']}")
            print(f"   Inputs: {entry['inputs']}")
            print(f"   Outputs: {entry['outputs']}\n")
    
    def add_import(self, imports):
        before = len(self._imports)
        if isinstance(imports, str):
            lines = imports.strip().split("\n")
        elif isinstance(imports, list):
            lines = imports
        else:
            raise TypeError("add_import() expects a string or list of strings.")
        for line in lines:
            cleaned = line.strip()
            if not cleaned:
                continue

            if not (cleaned.startswith("import ") or cleaned.startswith("from ")):
                raise ValueError(f"Invalid import statement: {cleaned}")

            self._imports.add(cleaned)
        after = len(self._imports)
        print(f"[QuickLearn] 📦 Registered {after - before} new import(s).")


    def _validate_dependencies(self, strict: bool = False):
        print("[QuickLearn] 🔍 Validating dependencies...")

        available_outputs = set()
        warnings = []

        for entry in self._committed:
            func_name = entry["func"].__name__
            inputs = entry["inputs"]
            outputs = entry["outputs"]

            # Check for missing inputs
            missing = [inp for inp in inputs if inp not in available_outputs]

            if missing:
                message = (
                    f"[QuickLearn Warning] '{func_name}' expects input(s) {missing} "
                    f"which were not produced by previous steps."
                )
                warnings.append(message)

            # Check for duplicate outputs
            duplicates = [out for out in outputs if out in available_outputs]
            if duplicates:
                message = (
                    f"[QuickLearn Warning] '{func_name}' produces duplicate output(s) {duplicates}."
                )
                warnings.append(message)

            available_outputs.update(outputs)

        if warnings:
            if strict:
                raise RuntimeError("\n".join(warnings))
            else:
                for w in warnings:
                    print(w)
                print(f"[QuickLearn] ⚠ {len(warnings)} warning(s) detected.")
        else:
            print("[QuickLearn] ✅ No dependency issues detected.")



    def compile(self, filename: str, validate: bool | str = True, group_comments: bool = True):

        if self._compiled:
            raise RuntimeError("Pipeline already compiled.")

        if not self._committed:
            raise RuntimeError("No committed functions found. Nothing to compile.")

        print(f"[QuickLearn] 🚀 Compiling {len(self._committed)} committed functions...")

        if validate:
            if validate == "strict":
                self._validate_dependencies(strict=True)
            else:
                self._validate_dependencies(strict=False)


        with open(filename, "w") as f:

            # Warn if no imports registered
            if not self._imports:
                print("[QuickLearn Warning] No imports registered. Compiled file may fail if dependencies are missing.")

            # Write registered imports
            for imp in sorted(self._imports):
                f.write(imp + "\n")

            if self._imports:
                f.write("\n\n")

            current_stage = None

            for entry in self._committed:

                if group_comments and entry["stage"] != current_stage:
                    current_stage = entry["stage"]
                    f.write("# ==============================\n")
                    f.write(f"# {current_stage}\n")
                    f.write("# ==============================\n\n")

                try:
                    source = inspect.getsource(entry["func"])
                except OSError:
                    raise RuntimeError(
                        f"Could not retrieve source for function '{entry['func'].__name__}'. "
                        "Ensure it is defined in a proper Python file or notebook cell."
                    )

                f.write(source)
                f.write("\n\n")

            f.write("if __name__ == '__main__':\n")
            f.write("    print('Pipeline ready.')\n")

        self._compiled = True
        print("[QuickLearn] ✅ Compilation successful.")
        print(f"[QuickLearn] 📄 Pipeline written to '{filename}'")


    def reset(self):
        self._committed.clear()
        self._compiled = False
        self._imports.clear()
        print("[QuickLearn] 🔄 Pipeline reset.")
