import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test1(self):
        results = emotion_detector('I am glad this happened')
        self.assertEqual(results['dominant_emotion'], 'joy')

    def test2(self):
        results = emotion_detector('I am really mad about this')
        self.assertEqual(results['dominant_emotion'], 'anger')

    def test3(self):
        results = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(results['dominant_emotion'], 'disgust')

    def test4(self):
        results = emotion_detector('I am so sad about this')
        self.assertEqual(results['dominant_emotion'], 'sadness')
    
    def test5(self):
        results = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(results['dominant_emotion'], 'fear')

unittest.main()