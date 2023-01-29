'''
public class Solution {
    private static class Node {
        public final boolean isDigitOne;
        public final int val;
        public final Node prev;
        public Node(boolean isDigitOne, int val, Node prev) {
            this.isDigitOne = isDigitOne;
            this.val = val;
            this.prev = prev;
        }
    }

    public String multiple(int num) {
        if (num < 0) {
            throw new IllegalArgumentException("Invalid args");
        }

        String result = "0";

        if (num > 0) {
            // A set to store all the visited nodes
            boolean[] isVisited = new boolean[num];
            Arrays.fill(isVisited, false);

            Set<Integer> visitedSet = new HashSet<>();
            // The queue used by BFS
            Queue<Node> queue = new ArrayDeque<>();

            // Add the first number 1 and mark it visited
            queue.add(new Node(true, 1 % num, null));
            isVisited[1 % num] = true;

            // The final destination node which represents the answer
            Node destNode = null;

            while (!queue.isEmpty()) {
                // Get the next node from the queue
                Node currNode = queue.remove();

                if (currNode.val == 0) {
                    // We have reached a valid multiple of num
                    destNode = currNode;
                    break;
                } else {
                    // Visit the next 2 neighbors
                    // Append 0 - (currNode.val * 10)
                    // Append 1 - (currNode.val * 10) + 1

                    // Append a '0'
                    int val1 = (currNode.val * 10) % num;
                    if (!isVisited[val1]) {
                        queue.add(new Node(false, val1, currNode));
                        isVisited[val1] = true;
                    }

                    // Append a '1'
                    int val2 = (val1 + 1);
                    if (val2 == num) {
                        val2 = 0;
                    }
                    if (!isVisited[val2]) {
                        queue.add(new Node(true, val2, currNode));
                        isVisited[val2] = true;
                    }
                }
            }

            // Trace the path from destination to source
            if (destNode == null) {
                throw new IllegalStateException("Result should not be null");
            } else {
                StringBuilder reverseResultBuilder = new StringBuilder();
                Node currNode = destNode;
                while (currNode != null) {
                    reverseResultBuilder.append(currNode.isDigitOne ? '1' : '0');
                    currNode = currNode.prev;
                }
                result = reverseResultBuilder.reverse().toString();
            }
        }

        return result;
    }



    // class Node{
    //     int val;
    //     boolean isBitSet;
    //     Node prev;
    //     public Node(int val, boolean isBitSet, Node prev){
    //         this.val = val;
    //         this.isBitSet = isBitSet;
    //         this.prev = prev;
    //     }
    // }

    // public String multiple(int A) {

    //     HashSet<Integer> visited = new HashSet<>();
    //     Queue<Node>q = new LinkedList<>();
    //     q.add(new Node(1%A, true, null));
    //     visited.add(1%A);

    //     Node distinationNode = null;

    //     while(!q.isEmpty()){
    //         Node curr = q.poll();


    //         if(curr.val == 0){
    //             distinationNode = curr;
    //             //System.out.println("val="+curr.val+", distinationNode="+distinationNode);
    //             break;
    //         }

    //         int val1 = (curr.val*10+0)%A;
    //         if(!visited.contains(val1)){
    //             visited.add(val1);
    //             q.add(new Node(val1, false, curr));
    //         }

    //         int val2 = (curr.val*10+1)%A;
    //         if(!visited.contains(val2)){
    //             visited.add(val2);
    //             q.add(new Node(val2, true, curr));
    //         }

    //         //System.out.println("val="+curr.val+", val1="+val1+", val2="+val2);

    //     }

    //     StringBuilder sb = new StringBuilder();
    //     Node curr = distinationNode;
    //     while(curr != null){
    //         if(curr.isBitSet){
    //             sb.append('1');
    //         }else{
    //             sb.append('0');
    //         }

    //         curr = curr.prev;
    //     }

    //     return sb.reverse().toString();
    // }
}


//TLE not working
// public class Solution {

//     public int mod(String curr, int A){

//         int i=0;
//         int currNum = 0;

//         while(i<curr.length()){
//             int lastDigit = curr.charAt(i) == '1' ? 1 :0;
//             currNum = currNum*10 + lastDigit;
//             currNum = currNum%A;
//             i++;
//         }

//         return currNum;
//     }

//     public String multiple(int A) {

//         Queue<String>q = new LinkedList<>();
//         q.add("1");
//         HashSet<Integer>visitedReminder = new HashSet<>();

//         while(!q.isEmpty()){
//             String curr = q.poll();

//             int reminder = mod(curr, A);
//             if(reminder == 0){
//                 return curr;
//             }

//             if(!visitedReminder.contains(reminder)){
//                 visitedReminder.add(reminder);
//                 String newStr1 = curr+"0";
//                 String newStr2 = curr+"1";
//                 q.add(newStr1);
//                 q.add(newStr2);
//             }
//         }

//         return "-1";
//     }
// }


'''