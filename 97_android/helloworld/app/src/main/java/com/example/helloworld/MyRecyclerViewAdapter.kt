package com.example.helloworld

import android.content.Context
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView

class MyRecyclerViewAdapter(val context: Context, val dogList: ArrayList<Dog>) :
    RecyclerView.Adapter<RecyclerView.ViewHolder>() {
    override fun onCreateViewHolder(p0: ViewGroup, p1: Int): RecyclerView.ViewHolder {
        val v: View = LayoutInflater.from(p0.context).inflate(R.layout.main2_dog_item, p0, false)
        return MyViewHolder(v)
    }

    override fun getItemCount(): Int {
        return dogList.size
    }

    override fun onBindViewHolder(p0: RecyclerView.ViewHolder, p1: Int) {
        (p0 as MyViewHolder).apply {
            dogBreed!!.text = dogList[p1].breed
            dogAge!!.text = dogList[p1].age
            dogGender!!.text = dogList[p1].gender
            val resourceId = context.resources.getIdentifier(dogList[p1].photo, "drawable", context.packageName)
            dogPhoto!!.setImageResource(resourceId)
        }
    }

    private class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        var dogBreed: TextView? = null
        var dogAge: TextView? = null
        var dogGender: TextView? = null
        var dogPhoto: ImageView? = null

        init {
            dogBreed = itemView.findViewById(R.id.dogBreedTextView)
            dogAge = itemView.findViewById(R.id.dogAgeTextView)
            dogGender = itemView.findViewById(R.id.dogGenderTextView)
            dogPhoto = itemView.findViewById(R.id.dogPhotoImg)
        }
    }

}