import subprocess

class VideoCreator(object):
    def __init__(self, page_name):
        self.page_name = page_name
    def get_audio_dur_sec(self, audio_filename):
        command = 'mediainfo '+audio_filename
        ret = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]
        dur = 0
        for item in ret.split('\n'):
            if 'Duration' in item:
                dur = item
        dur = dur.split(':')[1].strip()
        # mn-minute, s-sec, ms-millisec
        mmss = dur.split()
        mins = 0
        secs = 0
        if 'mn' in mmss[0]:
            mins = int(mmss[0].translate(None, 'mn'))
            if len(mmss) == 2:
                secs = int(mmss[1].translate(None, 's'))
        elif 's' in mmss[0]:
            secs = int(mmss[0].translate(None, 's'))
        return mins*60 + secs

    def download_images(self, image_links):





