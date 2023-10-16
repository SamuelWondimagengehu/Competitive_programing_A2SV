object Solution {
    def isPalindrome(s: String): Boolean = {
        val compared = s.filter(c => c.isLetter || c.isDigit).map(_.toLower)
        compared.reverse == compared
    }
}