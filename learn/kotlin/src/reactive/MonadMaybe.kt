import io.reactivex.Maybe
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {
    val maybeValue: Maybe<Int> = Maybe.just(14)
    maybeValue.subscribeBy(
            onComplete = { println("Complete Empty") },
            onError = { println("Error $it") },
            onSuccess = { println("Complete with value $it") }
    )
    val maybeEmpty: Maybe<Int> = Maybe.empty()
    maybeEmpty.subscribeBy(
            onComplete = { println("Complete Empty") },
            onError = { println("Error $it") },
            onSuccess = { println("Complete with value $it") }
    )
}