import java.util.Stack;

public class p1 {
    static private Stack<Integer>[][] stacks;
    int limit = 5;
    public p1(int rows, int columns) {
        this.stacks = new Stack[rows][columns];
        for (int i = 0; i < rows; i++) {
            for(int j = 0; j< columns; j++)
            stacks[i][j] = new Stack<>();
        }
    }

    public void push(int row, int column, int value) {
        stacks[row][column].push(value);
    }

    public static int size(int row,int column){
        return stacks[row][column].size();
    }

    public int pop(int row, int column) {
        return stacks[row][column].pop();
    }
    public int peek(int row, int column) {
        return stacks[row][column].peek();
    }

    public boolean isFull(int row,int col){
        if (stacks[row][col].size()>=limit) {
            return true;
        }
        return false;
    }
    
    public void sort(int row,int col) {
        Stack<Integer> MainStack = stacks[row][col];
        Stack<Integer> tempStack = new Stack<>();

        while (!MainStack.isEmpty()) {
            int top = MainStack.pop();

            while (!tempStack.isEmpty() && tempStack.peek() > top) {
                MainStack.push(tempStack.pop());
            }

            tempStack.push(top);
        }

        while (!tempStack.isEmpty()) {
            MainStack.push(tempStack.pop());
        }
    }

    public boolean isEmpty(int row, int column) {
        return stacks[row][column].isEmpty();
    }

    public static void main(String[] args) {
        p1 stackArray = new p1(3, 10);

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 10; j++) {
                if (!stackArray.isFull(i, j)) {
                    stackArray.push(i, j, 1);
                }

            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(stackArray.peek(i, j)+ " ");
            }
            System.out.println();
        }
        System.out.println("+++++++++");
        stackArray.push(0, 0, 5);

        System.out.println("___________");
        stackArray.sort(0, 0);
        
        int ssasa = size(0,0);
        System.out.println(ssasa);
        
        

    }
}