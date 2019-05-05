import io.reactivex.subjects.PublishSubject
import io.reactivex.subjects.Subject
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.async
import java.util.regex.Matcher
import java.util.regex.Pattern

fun main(args: Array<String>) {
    println("Initial Out put with a = 15, b = 10")
    val calculator = ReactiveCalculator(15, 10)
    println("""Enter a = <number> or b = <number> in separate lines
        exit to exit the program""")
    var line: String?
    do {
        line = readLine()
        GlobalScope.async { calculator.handleInput(line) }
    } while (line != null && !line.toLowerCase().contains("exit"))


}

class ReactiveCalculator(a: Int, b: Int) {
    val subjectCalc: Subject<ReactiveCalculator> = PublishSubject.create()
    var nums: Pair<Int, Int> = Pair(0, 0)

    init {
        nums = Pair(a, b)

        subjectCalc.subscribe {
            with(it) {
                calculateAddition()
                calculateSubstraction()
                calculateMultiplication()
                calculateDivision()
            }
        }
        subjectCalc.onNext(this)
    }

    private inline fun calculateDivision(): Double {
        val result = nums.first / (nums.second * 1.0)
        println("Div = $result")
        return result
    }

    private inline fun calculateMultiplication(): Int {
        val result = nums.first * nums.second
        println("Mul = $result")
        return result
    }

    private inline fun calculateSubstraction(): Int {
        val result = nums.first - nums.second
        println("Sub = $result")
        return result
    }

    private inline fun calculateAddition(): Int {
        val result = nums.first + nums.second
        println("Add = $result")
        return result
    }

    private inline fun modifyNumbers(a: Int = nums.first, b: Int = nums.second) {
        nums = Pair(a, b)
        subjectCalc.onNext(this)
    }

    suspend fun handleInput(line: String?) {
        if (!line.equals("exit")) {
            val pattern: Pattern = Pattern.compile("([a|b])(?:\\s)?=(?:\\s)?(\\d*)")
            var a: Int? = null
            var b: Int? = null
            val matcher: Matcher = pattern.matcher(line)

            if (matcher.matches() && matcher.group(1) != null && matcher.group(2) != null) {
                if (matcher.group(1).toLowerCase() == "a") {
                    a = matcher.group(2).toInt()
                } else {
                    b = matcher.group(2).toInt()
                }
            }

            when {
                a != null && b != null -> modifyNumbers(a, b)
                a != null -> modifyNumbers(a = a)
                b != null -> modifyNumbers(b = b)
                else -> println("Invalid Input")
            }
        }
    }
}
