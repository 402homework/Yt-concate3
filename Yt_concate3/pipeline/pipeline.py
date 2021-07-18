from .Steps.step import StepException    #相對路徑(這個資料夾裡面的開始)
class Pipeline:
    def __init__(self,steps):
        self.steps = steps

    def run(self,inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(data,inputs)
            except StepEcception as e:
                print('Exception happend:', e)
                break

