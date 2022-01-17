
class Solution {
    static boolean ispalindrome(String arr){
        for (int i =0 ; i< arr.length() ; i++ )
        {
            if (arr.charAt(i) != arr.charAt(arr.length()-1-i) )
            {
                return false ; 
            }
        }
        //System.out.println(arr);
        return true;
    }
    static int palindromepair(int N, String arr[]) {
        // code here
        
        for(int i=0 ; i< N-1 ; i++ )
        {
            for (int j =i+1 ; j<N ; j++)
            {
                String str = "";
                str = arr[i]+arr[j];
                if (ispalindrome(str)) return 1;
                str = arr[j]+arr[i];
                if (ispalindrome(str)) return 1;
                
            }
        }
        return 0;
    }
};
