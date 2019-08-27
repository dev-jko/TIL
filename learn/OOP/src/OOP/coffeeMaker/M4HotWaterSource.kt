package OOP.coffeeMaker

class M4HotWaterSource(
        private val api: CoffeeMakerAPI
) : HotWaterSource(), Pollable {

    override fun startBrewing() {
        api.setReliefValveState(CoffeeMakerAPI.VALVE_CLOSE)
        api.setBoilerState(CoffeeMakerAPI.BOILER_ON)
    }

    override fun isReady(): Boolean {
        val boilerStatus = api.getBoilerStatus()
        return boilerStatus == CoffeeMakerAPI.BOILER_NOT_EMPTY
    }

    override fun pause() {
        api.setBoilerState(CoffeeMakerAPI.BOILER_OFF)
        api.setReliefValveState(CoffeeMakerAPI.VALVE_OPEN)
    }

    override fun resume() {
        api.setBoilerState(CoffeeMakerAPI.BOILER_ON)
        api.setReliefValveState(CoffeeMakerAPI.VALVE_CLOSE)
    }

    override fun poll() {
        val boilerStatus = api.getBoilerStatus()
        if (isBrewing && boilerStatus == CoffeeMakerAPI.BOILER_EMPTY) {
            api.setBoilerState(CoffeeMakerAPI.BOILER_OFF)
            api.setReliefValveState(CoffeeMakerAPI.VALVE_CLOSE)
            declareDone()
        }
    }
}