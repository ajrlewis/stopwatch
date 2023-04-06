import time


class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __str__(self) -> str:
        elapsed_time = self.elapsed_time()
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        elapsed_time_str = f"{int(hours):0>2}:{int(minutes):0>2}:{seconds:05.2f}"
        return f"Elapsed time: {elapsed_time_str}"

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self) -> float:
        if self.start_time is None:
            raise ValueError("Stopwatch has not been started")
        elif self.end_time is None:
            return time.time() - self.start_time
        else:
            return self.end_time - self.start_time
