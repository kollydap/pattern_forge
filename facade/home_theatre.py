class TV:
    def turn_on(self):
        return "TV is ON"
    
    def set_input(self, source):
        return f"TV input set to {source}"

class SoundSystem:
    def turn_on(self):
        return "Sound system is ON"
    
    def set_volume(self, level):
        return f"Volume set to {level}"
    
    def set_surround_mode(self):
        return "Surround sound activated"

class StreamingDevice:
    def turn_on(self):
        return "Streaming device is ON"
    
    def play_movie(self, movie):
        return f"Playing {movie}"

class Lights:
    def dim(self):
        return "Lights dimmed to 20%"

class HomeTheaterFacade:
    def __init__(self, tv, sound, streaming, lights):
        self.tv = tv
        self.sound = sound
        self.streaming = streaming
        self.lights = lights
    
    def watch_movie(self, movie):
        results = []
        results.append(self.lights.dim())
        results.append(self.tv.turn_on())
        results.append(self.sound.turn_on())
        results.append(self.streaming.turn_on())
        results.append(self.tv.set_input("HDMI"))
        results.append(self.sound.set_volume(15))
        results.append(self.sound.set_surround_mode())
        results.append(self.streaming.play_movie(movie))
        return "\n".join(results)