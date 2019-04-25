//  https://www.acmicpc.net/problem/4673
//  셀프 넘버


package baekjoon


fun main(args: Array<String>) {
    val memo = Array(10001) { true }
    val sb = StringBuffer()
    for (i in 1..10000) {
        if (memo[i]) {
            sb.append("$i\n")
        }
        val t = selfNum(i)
        if (t != i && t <= 10000) {
            memo[t] = false
        }
    }
    println(sb.toString())
}

fun selfNum(num: Int): Int {
    var result = num
    var n = num
    while (n > 0) {
        result += n % 10
        n /= 10
    }
    return result
}