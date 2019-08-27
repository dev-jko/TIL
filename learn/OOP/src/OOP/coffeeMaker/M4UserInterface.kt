package OOP.coffeeMaker

class M4UserInterface(
        private val api: CoffeeMakerAPI
) : UserInterface(), Pollable {

    override fun poll() {
        val buttonStatus:Int = api.getBrewButtonStatus()
        if (buttonStatus == CoffeeMakerAPI.BREW_BUTTON_PUSHED) {
            startBrewing()
        }
    }

    override fun done() {
        api.setIndicatorState(CoffeeMakerAPI.INDICATOR_ON)
    }

    override fun completeCycle() {
        api.setIndicatorState(CoffeeMakerAPI.INDICATOR_OFF)
    }
}