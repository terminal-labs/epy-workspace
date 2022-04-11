from .unparse import Unparser


# For the Cython generator we re-use the Unparser code generator
# and generate Cython code instead for nodes that have type information
class CythonGenerator(Unparser):

    def get_type_from_comment(self, node):
        tp = self._type_ignores.get(node.lineno) or node.type_comment
        if tp is not None:
            return tp

    def visit_Assign(self, node):
         self.fill()
         for target in node.targets:
             if type_comment := self.get_type_from_comment(node):
                 self.write(f"cdef {type_comment} ")
             self.traverse(target)
             self.write(" = ")
         self.traverse(node.value)

    def visit_AnnAssign(self, node):
        self.fill()
        self.write("cdef ")
        self.traverse(node.annotation)
        self.write(" ")
        with self.delimit_if("(", ")", not node.simple and
                             isinstance(node.target, Name)):
            self.traverse(node.target)
        if node.value:
            self.write(" = ")
            self.traverse(node.value)

    def _function_helper(self, node, fill_suffix):
        self.maybe_newline()
        for deco in node.decorator_list:
            self.fill("@")
            self.traverse(deco)
        if node.returns:
            self.fill("cdef ")
            self.traverse(node.returns)
            self.write(" " + node.name)
        else:
            def_str = fill_suffix + " " + node.name
            self.fill(def_str)
        with self.delimit("(", ")"):
            self.traverse(node.args)
        with self.block(extra=self.get_type_from_comment(node)):
            self._write_docstring_and_traverse_body(node)

    def visit_arg(self, node):
         if node.annotation:
             self.traverse(node.annotation)
             self.write(" ")
         self.write(node.arg)
