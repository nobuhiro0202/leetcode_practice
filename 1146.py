class SnapshotArray:

    def __init__(self, length: int):
        self.current = {}
        self.history = []
        self.updated = True
        self.snap_counter = 0

    def set(self, index: int, val: int) -> None:
        self.current[index] = val
        self.updated = True

    def snap(self) -> int:
        snap_id = self.snap_counter
        
        if self.updated:
            self.history.append(dict(self.current))
            self.updated = False
        else:
            self.history.append(self.history[-1])
        
        self.snap_counter += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.history[snap_id].get(index, 0)