package com.example.daggerexample

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import com.example.daggerexample.databinding.ActivityMainBinding
import kotlinx.android.synthetic.main.activity_main.*
import javax.inject.Inject

class MainActivity : AppCompatActivity() {

    @Inject
    lateinit var cat: Cat

    @Inject
    lateinit var dog: Dog

    val binding: ActivityMainBinding by lazy {
        DataBindingUtil.setContentView<ActivityMainBinding>(this, R.layout.activity_main)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding.lifecycleOwner = this
        binding.vm = TestViewModel()


        injectComponent()

        setCatName()
        setDogName()
    }

    private fun injectComponent() {
        DaggerPetComponent.builder()
            .catModule(CatModule)
            .dogModule(DogModule)
            .build()
            .inject(this)
    }

    private fun setDogName() {
        tv2.text = dog.dogName
    }

    private fun setCatName() {
        tv1.text = cat.catName
    }


}
