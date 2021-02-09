class Node():
    def __init__(self):
        self.node=dict()
        self.parent=set()
    def addNode(self,node,cost=0):
        """[子ノードを追加します]
        Args:
            node (int): [子ノードの番号]
            cost (int, optional): [子ノードまでの移動コスト]. Defaults to 0.
        """
        self.node[node]=cost
    def addParent(self,node):
        """[指定したノードに親フラグを付けます]
        Args:
            node (int): [親フラグをつけるノードの番号]
        """