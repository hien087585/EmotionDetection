import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am very happy and excited")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I am very sad and depressed")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_empty(self):
        result = emotion_detector("")
        self.assertEqual(result["error"], "400")


if __name__ == "__main__":
    unittest.main()
