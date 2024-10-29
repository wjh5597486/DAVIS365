import dv_processing


class DVS:
    def __init__(self, args):
        # setting
        self.max_event_number = args.max_event_number
        self.fps = args.fps
        self.display_scale = args.display_scale

        # devices
        self.device = dv_processing.io.CameraCapture()
        self.slicer = dv_processing.EventMultiStreamSlicer("events")
        self.slicer.addFrameStream("frames")

        self.resolution = self.device.getEventResolution()
        self.noise_