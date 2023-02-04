public static List<Integer> gradingStudents(List<Integer> grades) {
    // Write your code here
        List<Integer> newList = new ArrayList<>();
        
        for(int i = 0; i < grades.size(); i++) {
            int grade = grades.get(i);
            
            if(grade < 38) {
                newList.add(grade);
            } else {
                int multiple = (grade / 5) + 1, mulOf5 = multiple * 5, diff = mulOf5 - grade;
                if(diff < 3) {
                    newList.add(grade + diff);
                } else {
                    newList.add(grade);  
                }    
            }
        }
        
        return newList;
    }

}
