class Dll:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Dll(homepage)

    def visit(self, url: str) -> None:
        self.vis = Dll(url)
        self.vis.prev = self.curr
        self.curr.next = self.vis
        self.curr = self.vis

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.prev:
            self.curr = self.curr.prev
            i += 1
        return self.curr.url    
        
    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.next:
            self.curr = self.curr.next
            i += 1
        return self.curr.url  
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)