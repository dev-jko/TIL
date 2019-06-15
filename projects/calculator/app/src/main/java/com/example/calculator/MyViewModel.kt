package com.example.calculator

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class MyViewModel : ViewModel() {

    companion object {
        const val Add = 0
        const val Subtract = 1
        const val Multiply = 2
        const val Divide = 3
    }

    private val myModel: MyModel = MyModel()

    private val _display = MutableLiveData("0")
    private var operator: Int = Add
    private var _result: Double = 0.0
    private var isDecimalPointUsed = false

    val display: LiveData<String> = _display


    fun appendNumberToDisplay(number: Int) {
        if (_display.value!!.length >= 20)
            return
        if (number == 10) {
            if (!isDecimalPointUsed) {
                _display.postValue(_display.value + ".")
                isDecimalPointUsed = true
            }
            return
        }
        if (_display.value == "0") {
            _display.postValue(number.toString())
            return
        }
        _display.postValue(_display.value + number.toString())
    }

    fun setOperator(operator: Int) {
        this.operator = operator
        _result = _display.value!!.toDouble()
        isDecimalPointUsed = false
        _display.postValue("0")
    }

    fun clearEntry() {
        isDecimalPointUsed = false
        _display.postValue("0")
    }

    fun clear() {
        _result = 0.0
        isDecimalPointUsed = false
        operator = Add
        _display.postValue("0")
    }

    fun deleteLastDisplayNum() {
        if (_display.value == "0")
            return
        if (_display.value!!.length <= 1) {
            _display.postValue("0")
            return
        }
        if (_display.value!![_display.value!!.length - 1] == '.')
            isDecimalPointUsed = false
        _display.postValue(_display.value!!.substring(0, _display.value!!.length - 1))
    }

    fun calculate() {
        val operand = _display.value!!.toDouble()
        val result = when (operator) {
            Add -> myModel.add(_result, operand)
            Subtract -> myModel.subtract(_result, operand)
            Multiply -> myModel.multiply(_result, operand)
            Divide -> myModel.divide(_result, operand)
            else -> 0.0
        }.toString()
        clear()
        if (result.contains('.'))
            isDecimalPointUsed = true
        _display.postValue(detachDecimalPointIfZero(result))
    }

    private fun detachDecimalPointIfZero(numberString: String): String {
        val length = numberString.length
        if (numberString.substring(length - 2, length) == ".0") {
            isDecimalPointUsed = false
            return numberString.substring(0, length - 2)
        }
        return numberString
    }


}
