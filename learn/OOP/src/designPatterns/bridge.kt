package designPatterns

fun main() {
    val bow = Bow()
    val sword = Sword()

    val warrior = Warrior(bow)
    warrior.handle()
    warrior.weapon = sword
    warrior.handle()
    warrior.eat()

    val smith = Smith(bow)
    smith.handle()
    smith.weapon = sword
    smith.handle()
    smith.drink()
}

interface Weapon {
    fun attack()
    fun repair()
}

interface WeaponHandler {
    fun handle()
}

class Warrior(var weapon: Weapon) : WeaponHandler {
    override fun handle() {
        print("designPatterns.Warrior ")
        this.weapon.attack()
    }

    fun eat(){
        println("designPatterns.Warrior Eat")
    }
}

class Smith(var weapon: Weapon) : WeaponHandler {
    override fun handle() {
        print("designPatterns.Smith ")
        this.weapon.repair()
    }

    fun drink(){
        println("designPatterns.Smith Drink")
    }
}

class Bow : Weapon {
    override fun attack() {
        println("designPatterns.Bow Attack")
    }

    override fun repair() {
        println("designPatterns.Bow Repair")
    }
}

class Sword : Weapon {
    override fun attack() {
        println("designPatterns.Sword Attack")
    }

    override fun repair() {
        println("designPatterns.Sword Repair")
    }
}