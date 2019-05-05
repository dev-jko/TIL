import io.reactivex.Observable
import io.reactivex.Observer
import io.reactivex.disposables.Disposable
import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    val observer: Observer<Any> = object : Observer<Any> {
        override fun onComplete() {
            println("All Completed")
        }

        override fun onSubscribe(d: Disposable) {
            println("Subscribed to $d")
        }

        override fun onNext(t: Any) {
            println("Next $t")
        }

        override fun onError(e: Throwable) {
            println("Error Occurred $e")
        }
    }

    val observable: Observable<Any> = listOf("One", 2, "Three", 4.5, 6.0f).toObservable()

    observable.subscribe(observer)

    val observableOnList: Observable<List<Any>> = Observable.just(
            listOf("One", 2, 4.5),
            listOf(1, 2, 3, 4, 5, 6, 7, 8),
            listOf("List with Single Item")
    )
    observableOnList.subscribe(observer)

}