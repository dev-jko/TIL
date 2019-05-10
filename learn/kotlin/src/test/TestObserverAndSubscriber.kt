package test

import io.reactivex.observers.TestObserver
import io.reactivex.rxkotlin.toFlowable
import io.reactivex.rxkotlin.toObservable
import io.reactivex.subscribers.TestSubscriber
import org.junit.Test

class TestObserverAndSubscriber {
    @Test
    fun `test with TestObserver`() {
        val list = listOf(12, 5, 6, 7, 8, 5, 32, 1, 24, 5, 43, 6, 7, 8, 4, 4, 31)
        val observable = list.toObservable().sorted()
        val testObserver = TestObserver<Int>()
        observable.subscribe(testObserver)

        testObserver.assertSubscribed()

        testObserver.awaitTerminalEvent()
        testObserver.assertNoErrors()
        testObserver.assertComplete()
        testObserver.assertValueCount(17)
        testObserver.assertValues(1, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 12, 24, 31, 32, 43)
    }

    @Test
    fun `test with TestSubscriber`() {
        val list = listOf(12, 5, 6, 7, 8, 5, 32, 1, 24, 5, 43, 6, 7, 8, 4, 4, 31)
        val flowable = list.toFlowable().sorted()
        val testSubscriber = TestSubscriber<Int>()
        flowable.subscribe(testSubscriber)

        testSubscriber.assertSubscribed()

        testSubscriber.assertNoErrors()
        testSubscriber.assertComplete()
        testSubscriber.assertValueCount(17)
        testSubscriber.assertValues(1, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 12, 24, 31, 32, 43)
    }
}