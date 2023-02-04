class Solution {
    public String sortSentence(String s) {
        Map<Integer,String> indexWordMap = new HashMap();

        for(String str : s.split(" ")) {
            int lastIndex = str.length() - 1;

            int index = str.charAt(lastIndex) - '0';
            String actualWord = str.substring(0, lastIndex);

            indexWordMap.put(index,actualWord);
        }

        StringBuilder actualString = new StringBuilder();
        for(Map.Entry<Integer,String> indexWord : indexWordMap.entrySet()) {
            actualString.append(indexWord.getValue());
            actualString.append(" ");
        }

        return actualString.toString().trim();
    }
}
