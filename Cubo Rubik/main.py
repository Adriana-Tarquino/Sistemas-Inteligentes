from RubiksCube import RubiksCube

if __name__ == "__main__":
    
    cube = [ 
            #white up
             [ ['W','W','W'],
               ['W','W','W'],
               ['W','W','W']  ],
            #green front
             [ ['G','G','G'],
               ['G','G','G'],
               ['G','G','G']  ],
            #red right
            [  ['R','R','R'],
               ['R','R','R'],
               ['R','R','R']  ],
            #blue back
            [  ['B','B','B'],
               ['B','B','B'],
               ['B','B','B']  ],
            #orange left
            [  ['O','O','O'],
               ['O','O','O'],
               ['O','O','O']  ],
            #yelow down
            [  ['Y','Y','Y'],
               ['Y','Y','Y'],
               ['Y','Y','Y']  ],
            
            ]
    RubiksCube(cube)
    
    