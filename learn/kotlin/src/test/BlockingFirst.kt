package test

import io.reactivex.rxkotlin.toObservable
import org.junit.Test
import kotlin.test.assertEquals

class BlockingFirst {

    @Test
    fun `test with blockingFirst`() {
        val observable = listOf(5, 2, 67, 8, 3, 2, 3, 5, 1, 5).toObservable().sorted()
        val firstItem = observable.blockingFirst()
        assertEquals(1, firstItem)
    }
}