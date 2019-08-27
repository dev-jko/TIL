package OOP.coffeeMaker

interface CoffeeMakerAPI {

    companion object {
        const val WARMER_EMPTY = 0
        const val POT_EMPTY = 1
        const val POT_NOT_EMPTY = 2

        const val BOILER_EMPTY = 0
        const val BOILER_NOT_EMPTY = 1

        const val BREW_BUTTON_PUSHED = 0
        const val BREW_BUTTON_NOT_PUSHED = 1

        const val BOILER_ON = 0
        const val BOILER_OFF = 1

        const val WARMER_ON = 0
        const val WARMER_OFF = 1

        const val INDICATOR_ON = 0
        const val INDICATOR_OFF = 1

        const val VALVE_OPEN = 0
        const val VALVE_CLOSE = 1
    }

    fun getWarmerPlateStatus(): Int
    fun getBoilerStatus(): Int
    fun getBrewButtonStatus(): Int
    fun setBoilerState(boilerState: Int)
    fun setWarmerState(warmerState: Int)
    fun setIndicatorState(indicatorState: Int)
    fun setReliefValveState(valveState: Int)
}
