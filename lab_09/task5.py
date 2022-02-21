# 5. Напишіть функцію, яка поверне кількість слів у рядку тексту.

import unittest
import string

def wordcount(*strings: str) -> int:
  # Type checking
  if not all(isinstance(string, str) for string in strings):
    raise Exception('All input variables must be of type str')

  word_count = 0

  # Preparing exclude list
  exclude_list = list(string.digits) + list(string.punctuation)

  # Calculating word count
  for element in strings:
    words = element.split(" ")

    for word in words:
      if not all((letter in exclude_list) for letter in list(word)):
        word_count += 1

  return word_count

# Tests
class TestCase(unittest.TestCase):
  def test_1(self):
    return self.assertEqual(wordcount(""), 0)

  def test_2(self):
    return self.assertEqual(wordcount("rutrum quisque non tellus orci", "rutrum quisque non tellus orci"), 10)

  def test_3(self):
    return self.assertEqual(wordcount(", . _ 0 1 2 3 4 5 6 7 8 9 * & ^ %"), 0)

  def test_4(self):
    return self.assertEqual(wordcount("word: i'm"), 2)

  def test_5(self):
    return self.assertEqual(wordcount("два слова"), 2)

  def test_6(self):
    return self.assertEqual(wordcount("вот . , 1,2 три слова"), 3)

  # Error checking
  def test_7(self):
    with self.assertRaises(Exception):
      wordcount(0)

  def test_8(self):
    with self.assertRaises(Exception):
      wordcount(0, 1, 2, 3)

  def test_9(self):
    with self.assertRaises(Exception):
      wordcount(("tuple", "of", "strings"), ("are", "not", "allowed", "too", ":c"))

unittest.main()