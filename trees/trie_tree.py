#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : trie_tree.py
@Time : 4/22/22 10:42 PM
@Desc: 
"""


class TrieNode:
    """
    A class for Trie node
    """

    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    """
    A class for Trie
    """

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        """
        Get the Node
        :return:
        """
        return TrieNode()

    def _char_to_index(self, ch):
        """
        Converts key current character into index
        :param ch:
        :return:
        """
        return ord(ch) - ord('a')

    def insert(self, key):
        """
        Insert char to tries
        :param key:
        :return:
        """
        p_crawl = self.root
        length = len(key)
        print(length)
        for level in range(length):
            index = self._char_to_index(key[level])
            print("index", index)
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]
        p_crawl.is_end_of_word = True

    def search(self, key):
        """
        Search the char to tries tree
        :param key:
        :return:
        """
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]

        return p_crawl.is_end_of_word


def main():
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]
    t = Trie()
    for key in keys:
        t.insert(key)
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()
