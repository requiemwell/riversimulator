#!/usr/bin/env python
# coding: UTF-8

from unittest import TestCase, main

from river import River


class TestMethods(TestCase):
    r = River(3)
    r.setSeed(1)

    def testCreateRiver(self):
        self.r.createRiver(3)
        self.assertEqual(str(self.r.river), '[BF7, BM7, BF7]')
        self.assertNotEqual(str(self.r.river), '[BF7, BM6, BF7]')

    def testSetSeed(self):
        self.r.setSeed(0)
        self.assertEqual(self.r.seed, 0)
        self.r.setSeed(4)
        self.assertEqual(self.r.seed, 4)

    def testGetLength(self):
        self.assertEqual(self.r.getLength, 3)

    def testUpdateCell(self):
        pass

    def testUpdateRiver(self):
        self.r.updateRiver()
        self.assertEqual(str(self.r.river[0]), 'BF8')
        self.assertEqual(str(self.r.river[1]), 'BM8')
        self.assertEqual(str(self.r.river[2]), 'BF0')


if __name__ == "__main__":
    main()
