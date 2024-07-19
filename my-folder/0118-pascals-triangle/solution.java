class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascal = new ArrayList<>();
        List<Integer> firstRow = new ArrayList<>();
        firstRow.add(1);
        pascal.add(firstRow);
        int currentRow = 1;
        
        while(currentRow < numRows){
            List<Integer> row = new ArrayList<>();
            List<Integer> prevRow = pascal.get(currentRow-1);
            row.add(1);
            for(int i=1; i<=currentRow-1; i++){
                row.add(prevRow.get(i-1) + prevRow.get(i));
            }
            row.add(1);
            pascal.add(row);
            currentRow ++;
        }
        return pascal;
    }
}
