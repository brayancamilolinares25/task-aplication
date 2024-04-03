import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

void main(){
  runApp(MainApp());
}

class MainApp extends StatelessWidget{
  MainApp({super.key});

  @override
  Widget build(BuildContext context){
    return MaterialApp(
    debugShowCheckedModeBanner: false,
     home: Scaffold(
      body: Text("Task aplication"),
     ),
    );
  }
}
