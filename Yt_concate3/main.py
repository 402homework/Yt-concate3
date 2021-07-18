from Yt_concate3.pipeline.Steps.get_video_list import GetVideoList
from Yt_concate3.pipeline.Steps.step import StepException
from Yt_concate3.pipeline.pipeline import Pipeline


CHANNEL_ID = 'UCGGrblndNzi86WY5lJkQJiA'
def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList()

             ]
    p = Pipeline(steps)
    p.run(inputs)

if __name__ == '__main__':
    main()



