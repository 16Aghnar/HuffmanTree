# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:29:09 2017

@author: Sony
"""

#Huffman
test = "Well, there's egg and bacon; egg sausage and bacon, egg and spam; egg bacon and spam; egg bacon sausage and spam; spam bacon sausage and spam; spam egg spam spam bacon and spam; spam sausage spam spam bacon spam tomato and spam."


class Node:
    
    def __init__(self, char, freq, left=None, right=None, is_leaf=False):
        self.left = left
        self.right = right
        self.char = char
        self.freq = freq
        self.is_leaf = is_leaf
        
    def __lt__(self, other):
        return (self.freq < other.freq)
   
     
class Huffman_Code:
    
    def frequencies(self, message):
        freqs = {}
        for char in message:
            if not char in freqs :
                freqs[char] = 0
            freqs[char] += 1
        return freqs
    
    def get_minimal_node(self, tree):
        if len(tree) == 1:
            return 0
        if len(tree) == 0:
            return -1
        
        min_a = 0
        for i,v in enumerate(tree):
            if v<tree[min_a] :
                min_a = i
        return min_a
    
    def Tree(self, freqs):
        tree = list()
        for char in freqs:
            tree.append(Node(char, freqs[char], is_leaf=True))
        
        while(len(tree)>1):
            min_a = self.get_minimal_node(tree)
            node1 = tree.pop(min_a)
            min_b = self.get_minimal_node(tree)
            node2 = tree.pop(min_b)
            new_node = Node(node1.char + node2.char, node1.freq + node2.freq,
                            node1, node2)
            tree.append(new_node)
            
        return tree[0]
    
    def code(self, tree, freqs):
        code = {}
        for key in freqs:
            current_node = tree
            sequence = ''
            while not(current_node.is_leaf) :
                if key in current_node.left.char :
                    sequence += '0'
                    current_node = current_node.left

                elif key in current_node.right.char :
                    sequence += '1'
                    current_node = current_node.right
                else :
                    raise Exception
            code[key] = sequence
        return code
    
    def encode(self, codex, text):
        binary_code = ''
        for char in text :
            binary_code += codex[char]
        return binary_code
        
    def decode(self, codex, binary_code):
        text = ''
        bin_code = binary_code
        while len(bin_code)>0:
            index = 1
            next_char = False
            while not next_char:
                for key in codex:
                    if codex[key] == bin_code[:index]:
                        text += key
                        next_char = True
                index += 1
            bin_code = bin_code[index-1:]
        return text
        
    
    def __init__(self, text):
        self.text = text


if __name__ =='__main__' :

    test = input('Que voulez-vous coder?')
    hc = Huffman_Code(test)
    freqs = hc.frequencies(test)
    tree = hc.Tree(freqs)
    codex = hc.code(tree, freqs)
    
    coded_text = hc.encode(codex, test)
    print(coded_text)
    decoded_text = hc.decode(codex, coded_text)
    print(decoded_text)
    
    print('\nThe decoded text is the same as the original : ' + str(decoded_text == hc.text))
    print('length text :', len(hc.text),'; length coded_text :', len(coded_text))
    print('Compression rate =', len(coded_text)/(len(hc.text)*8))
    
