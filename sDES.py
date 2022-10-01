'''
>	@author Juan Manuel Nava Rosales
>	@date 01/octubre/2022
>	@brief sDES Algorithm - Cryptography - Practice 3
>	@version 1.0 
'''

def initPermutation( txt ): #(1,5,2,0,3,7,4,6)
  return txt[1]+txt[5]+txt[2]+txt[0]+txt[3]+txt[7]+txt[4]+txt[6]

def subKeys( key ): #(2,4,1 6,3 9,0 8,7 5)
  permut = key[2]+key[4]+key[1]+key[6]+key[3]+key[9]+key[0]+key[8]+key[7]+key[5]
  sk, sk2 = permut[1:5]+permut[0], permut[6:]+permut[5] #cyclically shifted one bit
  sk = sk + sk2 # (5,2,6,3,7,4,9,8) -> SubkeyOne
  sk2 = sk[2:5]+sk[:2]+sk[7:]+sk[5:7] #(5,2,6,3,7,4,9,8) -> SubkeyTwo
  return sk[5]+sk[2]+sk[6]+sk[3]+sk[7]+sk[4]+sk[9]+sk[8], sk2[5]+sk2[2]+sk2[6]+sk2[3]+sk2[7]+sk2[4]+sk2[9]+sk2[8]

def feistel( sk ):
  k1, k2 = sk[:5], sk[5:]

  return

def switch():
  return

def inversePermutation():
  return

def sDES( text, key ):
  subkey1, subkey2 = subKeys( key )
  # Encrypt
  permutOne = initPermutation( text ) # Step 1
  feistelsk = feistel( subkey1 )      # Step 2

  #print(permutOne)
  print(subkey1)
  print(subkey2)

def main():
  sDES("01010101","0000011111")


if __name__ == "__main__":
	main()