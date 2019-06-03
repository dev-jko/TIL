

fun main() {

    val num1: Int = 2
    val num2: Int = 3

    val result1: Int = plus(num1, num2)
    val result2: Int = { a: Int, b: Int -> a + b }(num1, num2)

    println("function : $num1 + $num2 = $result1")
    println("lambda function : $num1 + $num2 = $result2")


    val array = arrayOf(1, 2, 3, 4, 5)
    var result = 0

    for (n in array) {
        result += n
    }
    println(result)

    result = 0
    array.forEach { result += it }
    println(result)

    result = 0
    result = array.reduce { acc, i -> acc + i }
    println(result)
}


fun plus(a: Int, b: Int): Int {
    return a + b
}