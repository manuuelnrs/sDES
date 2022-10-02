'''
>	@author Juan Manuel Nava Rosales
>	@date 01/octubre/2022
>	@brief sDES Algorithm - Cryptography - Practice 3
>	@version 1.0 
'''

from math import perm


def initPermutation( txt ): #(1,5,2,0,3,7,4,6)
  return txt[1]+txt[5]+txt[2]+txt[0]+txt[3]+txt[7]+txt[4]+txt[6]

def subKeys( key ): #(2,4,1 6,3 9,0 8,7 5)
  permut = key[2]+key[4]+key[1]+key[6]+key[3]+key[9]+key[0]+key[8]+key[7]+key[5]
  sk, sk2 = permut[1:5]+permut[0], permut[6:]+permut[5] #cyclically shifted one bit
  sk = sk + sk2 # (5,2,6,3,7,4,9,8) -> SubkeyOne
  sk2 = sk[2:5]+sk[:2]+sk[7:]+sk[5:7] #(5,2,6,3,7,4,9,8) -> SubkeyTwo
  return sk[5]+sk[2]+sk[6]+sk[3]+sk[7]+sk[4]+sk[9]+sk[8], sk2[5]+sk2[2]+sk2[6]+sk2[3]+sk2[7]+sk2[4]+sk2[9]+sk2[8]

def feistel( sk, permutOne ):
  lh, rh = permutOne[:4], permutOne[4:] # left and right halves
  expanded = rh[3]+rh[0]+rh[1]+rh[2]+rh[1]+rh[2]+rh[3]+rh[0]
  xored = str(bin(int(expanded,2) ^ int(sk,2)))
  xored = xored[2:].zfill(8)            # formated to 8-bit binary
  mix = Sbox( xored[:4], xored[4:] )
  mix = mix[1]+mix[3]+mix[2]+mix[0]     #permuted
  mix = str(bin(int(mix,2) ^ int(lh,2)))
  mix = mix[2:].zfill(4)                # formated to 4-bit binary
  return mix + rh                       # concated

def Sbox( lhalve, rhalve ):
  box  = [[1,0,3,2], [3,2,1,0], [0,2,1,3], [3,1,3,2]]
  intBox = str(bin(box[int(lhalve[0]+lhalve[3],2)][int(lhalve[1:3],2)]))
  box2 = [[0,1,2,3], [2,0,1,3], [3,0,1,0], [2,1,0,3]]
  intBox2 = str(bin(box2[int(rhalve[0]+rhalve[3],2)][int(rhalve[1:3],2)]))
  concat = intBox[2:].zfill(2) + intBox2[2:].zfill(2) # formated to 4-bit binary
  return concat

def inversePermutation( intxt ): #(3,0,2,4,6,1,7,5)
  return intxt[3]+intxt[0]+intxt[2]+intxt[4]+intxt[6]+intxt[1]+intxt[7]+intxt[5]

def sDES( text, key ):
  subkey1, subkey2 = subKeys( key ) # 8-bit
  # Encrypt
  permutOne = initPermutation( text )     # Step 1
  blockMix = feistel( subkey1, permutOne )# Step 2
  blockMix = blockMix[4:]+blockMix[:4]    # Step 3
  blockMix = feistel( subkey2, blockMix ) # Step 4
  return inversePermutation( blockMix )   # Step 5

def main():
  print("\tsDES Algorithm - Practical Session 3 - 419048901")
  #PlainText and Key 10-bit
  plainText = "01010101"
  Key10 = "0000011111"
  ciphertext = sDES( plainText, Key10 )
  print("TEST_VECTOR(1)")
  print(f"PlainText: {plainText} and Key: {Key10} => CipherText: {ciphertext}")
  #11000100
  
  plainText = "00110110"
  Key10 = "0010010111"
  ciphertext = sDES( plainText, Key10 )
  print("TEST_VECTOR(2)")
  print(f"PlainText: {plainText} and Key: {Key10} => CipherText: {ciphertext}")
  #01011010
  
  plainText = "00000000"
  Key10 = "0000000000"
  ciphertext = sDES( plainText, Key10 )
  print("TEST_VECTOR(3)")
  print(f"PlainText: {plainText} and Key: {Key10} => CipherText: {ciphertext}")
  #11110000
  
  plainText = "11111111"
  Key10 = "1111111111"
  ciphertext = sDES( plainText, Key10 )
  print("TEST_VECTOR(4)")
  print(f"PlainText: {plainText} and Key: {Key10} => CipherText: {ciphertext}")
  #00001111

if __name__ == "__main__":
	main()