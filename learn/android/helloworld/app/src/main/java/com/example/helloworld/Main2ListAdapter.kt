package com.example.helloworld

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.ImageView
import android.widget.TextView

class Main2ListAdapter(val context: Context, val dogList: ArrayList<Dog>) : BaseAdapter() {
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View
        val holder: ViewHolder

        if (convertView == null) {
            view = LayoutInflater.from(context).inflate(R.layout.main2_dog_item, null)
            holder = ViewHolder()
            holder.dogPhoto = view.findViewById(R.id.dogPhotoImg)
            holder.dogBreed = view.findViewById(R.id.dogBreedTextView)
            holder.dogAge = view.findViewById(R.id.dogAgeTextView)
            holder.dogGender = view.findViewById(R.id.dogGenderTextView)
            view.tag = holder
        } else {
            holder = convertView.tag as ViewHolder
            view = convertView
        }

        val dog = dogList[position]
        val resourceId = context.resources.getIdentifier(dog.photo, "drawable", context.packageName)
        holder.dogPhoto?.setImageResource(resourceId)
        holder.dogBreed?.text = dog.breed
        holder.dogAge?.text = dog.age
        holder.dogGender?.text = dog.gender
        return view
    }

    override fun getItem(position: Int): Any {
        return dogList[position]
    }

    override fun getItemId(position: Int): Long {
        return 0
    }

    override fun getCount(): Int {
        return dogList.size
    }


    private class ViewHolder {
        var dogBreed: TextView? = null
        var dogAge: TextView? = null
        var dogGender: TextView? = null
        var dogPhoto: ImageView? = null
    }

}