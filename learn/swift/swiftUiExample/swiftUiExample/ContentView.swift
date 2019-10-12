//
//  ContentView.swift
//  HitMeGame_SwiftUI
//
//  Created by Jinyung Yoon on 01/10/2019.
//  Copyright © 2019 Jinyung Yoon. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    
    @State var alertIsVisible: Bool = false
    @State var alertIsVisible2: Bool = false
    @State var sliderValue: Double = 0.0
    @State var answer: String = ""
    @State var target = Int.random(in: 0...100)
    @State var score = 0
    @State var stage = 1
    @State var point = 0
    @State var check = false
    @State var FinalPoint: [Int] = [0]
    @State var ranking = ""
    var timer: Timer {
        .scheduledTimer(withTimeInterval: 0.01, repeats: true) {_ in
            self.sliderValue += 1.0
            self.sliderValue = Double(Int(self.sliderValue) % 100)
        }
    }
    
    func pauseTimer() {
        print("hoi")
        self.timer.invalidate()
    }
    func restartTimer() {
        self.sliderValue = 0.0
        timer.fire()
    }
    
    struct LableStyle: ViewModifier {
        func body(content: Content) -> some View {
            return content
                .foregroundColor(Color.white)
                .shadow(color: Color.black, radius: 5, x: 2, y: 3)
                .font(Font.custom("Arial Rounded MT Bold", size: 18))
        }
    }
    
    struct ScoreStyle: ViewModifier {
        func body(content: Content) -> some View {
            return content
                .foregroundColor(Color.yellow)
                .shadow(color: Color.black, radius: 5, x: 2, y: 3)
                .font(Font.custom("Arial Rounded MT Bold", size: 18))
        }
    }
    
    var body: some View {
        VStack {
            HStack{
                Spacer()
                Button (action: {
                    self.alertIsVisible2 = true
                    if self.ranking == "" {
                        self.ranking = "아직 등록된 기록이 없습니다. \n 도전하셔서 1등을 차지하세요!"
                    }
                }) {
                    HStack {
                        Text("🏆 RANK")
                    }.font(Font.system(size: 12)).padding(.top, 10)
                }
                .alert(isPresented: $alertIsVisible2) { () ->
                    Alert in
                    return Alert(title: Text("Ranking"), message: Text("\(self.ranking)"), dismissButton: .default(Text("Ok")))
                }
                if FinalPoint.max()! == 0 {
                    
                } else {
                    Text(" 최고기록: \(FinalPoint.max()!)").font(Font.system(size: 12))
                }
            }
            
            Spacer()
            // Target row
            HStack {
                Text("Put the bullseyes as close as you can to: ").modifier(LableStyle())
                Text("\(self.target)").modifier(ScoreStyle())
//                Text("\(Int(sliderValue.rounded()))")
            }
            Spacer()
            // Slider row
            HStack {
                Text("1").modifier(LableStyle())
                Slider(value: self.$sliderValue, in: 1...100).accentColor(Color.green)
                Text("100").modifier(LableStyle())
            }
            Spacer()
            // Button row
            Button(action: {
//                self.alertIsVisible = true
//                self.score += self.gameResult()
//                self.check = true
                self.pauseTimer()
            }) {
                Text("Hit Me!")
            }
            .alert(isPresented: $alertIsVisible) { () ->
                Alert in
                return Alert(title: Text("Hello there!"), message: Text("Your choice is \(Int(self.sliderValue))\n" + "You get \(self.point) points"), dismissButton: .default(Text("\(self.answer)")) {
                        print(self.answer)
                        self.target = Int.random(in: 1...100)
                        self.stage += 1
                    if self.stage == 11 {
                        self.FinalPoint.append(self.score)
                        self.makeRanking()
                        self.reset()
//                        self.restartTimer()
                        self.check = false
                    }
                    })
            }
            .background(Image("Button")).modifier(ScoreStyle())
            
            Spacer()
            // Score row
            
            HStack {
                Button(action: {
                    self.reset()
                }) {
                    HStack {
                        Image("StartOverIcon")
                        Text("Start over")
                    }.font(Font.system(size: 12))
                }
                .background(Image("Button")).modifier(ScoreStyle())
                Spacer()
                Text("Score: ")
                Text("\(self.score)")
                Spacer()
                Text("Round: ")
                Text("\(self.stage) / 10")
                Spacer()
                
                
                
                NavigationLink(destination: AboutView()) {
                    HStack {
                        Image("InfoIcon")
                        Text("Info")
                    }.font(Font.system(size: 12))
                }
                    .onAppear(perform: { _ = self.timer})
                .background(Image("Button")).modifier(ScoreStyle())
            }
            .padding(.bottom, 20)
        }
        .background(Image("Background"), alignment: .center)
    .navigationBarTitle("Bullseye")
    }
    
    func reset() {
        target = Int.random(in: 1...100)
        score = 0
        stage = 1
    }
    
    func gameResult() -> Int {
        if Int(self.sliderValue) == self.target {
            self.answer = "Perfect"
            self.point = 100
        } else if abs(Int(self.sliderValue) - self.target) < 5 {
            self.answer = "Such a close"
            self.point = 50
        } else {
            self.answer = "Try again"
            self.point = 0
        }
        return self.point
    }
    
    func makeRanking() {
        if FinalPoint.count > 11 {
            for rank in 1...10 {
                self.ranking += "\(rank) 등 :\(FinalPoint[rank]) points"
            }
        } else {
            for rank in 1..<FinalPoint.count {
                self.ranking += "\(rank) 등 :\(FinalPoint[rank]) points"
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView().previewLayout(.fixed(width: 896, height: 414))
    }
}
