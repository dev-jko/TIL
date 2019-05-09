package test

import org.junit.Test
import kotlin.test.assertEquals

class TestClass {
    @Test
    fun `my first test`() {
        assertEquals(3, 1 + 2, "Actual value is not equal to the expected one.")
    }
}