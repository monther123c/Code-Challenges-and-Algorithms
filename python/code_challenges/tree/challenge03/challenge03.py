# Write here the code challenge solution
class Node :

    def __init__(self,value,left=None,right=None) -> None:
        self.value=value 
        self.right=right
        self.left=left

class Tree:

    def __init__(self) -> None:
        self.tree_list=[]

    def convert_to_bts(self,nums):

        '''
        convert the given list to a balanced BST
        params: list
        return:root
        
        '''



        idx=len(nums)//2

        if  not nums:

            return None
        
        left= nums[:idx]
        right=nums[idx+1:]
        root=Node(nums[idx],self.convert_to_bts(left),self.convert_to_bts(right))   

        return root


 
    def display_tree(self,root):

                '''
                params: root
                    
                return : all the roots values as a list 
                '''
                
            
                if not root:

                    return ['null']               
                    
                
                
                if root :

                    if root.left:

                        
                        self.tree_list.append(root.left.value)
                        try:
                            self.tree_list.append(root.right.value)
                        except AttributeError:
                            self.tree_list.append('null')
                    

                    else:

                        if not root.left:
                            self.tree_list.append('null')
                    
                        if not root.right:
                            self.tree_list.append('null')

                    self.display_tree(root.left)  
                    self.display_tree(root.right)   
                
               

                return self.tree_list 
