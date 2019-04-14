# Java面试学习日报书
-------

# 2019/04/10

-------

### 今日完成事宜
- [x] Java容器

   Arraylist 与 LinkedList 异同

    补充：数据结构基础之双向链表

   ArrayList 与 Vector 区别

    HashMap的底层实现

        JDK1.8之前

        JDK1.8之后

    HashMap 和 Hashtable 的区别

    HashMap 的长度为什么是2的幂次方

    HashMap 多线程操作导致死循环问题

    HashSet 和 HashMap 区别

    ConcurrentHashMap 和 Hashtable 的区别

    ConcurrentHashMap线程安全的具体实现方式/底层具体实现

        JDK1.7（上面有示意图）

        JDK1.8 （上面有示意图）

    集合框架底层数据结构总结

    Collection

        1. List
        
        2. Set
        
    Map

- [ ] Java类加载机制 


-----
### 今日未完成事宜


| 事宜     |预期结果| 当前结果  | 未完成原因   | 
| --------   | -----:  | -----:  | :----:  |
|  Java类加载机制  | 全部看完 | 看到类验证阶段 | Java容器部分内容很多 |


------
### 明日待办事宜
- [ ] Java类加载机制
- [ ] 可能要开始进行课题二技术报告
- [ ] Java并发

-------
# 2019/04/11

-------

### 今日完成事宜
- [x]  Java类加载机制
 
 类加载过程：加载，验证，准备，解析，初始化，使用，卸载，其中前五步为关键步骤。
 
 ClassLoad类加载器

 双亲委派原则


- [x]  Java并发
 AQS CAS AQS同步组件


 乐观锁悲观锁


 容器的并发

-----
### 今日未完成事宜


| 事宜     |预期结果| 当前结果  | 未完成原因   | 
| --------   | -----:  | -----:  | :----:  |
| 红黑树  | 看完  |了解  |太难  |


------
### 明日待办事宜
- [ ] Spring 
- [ ] AOP

-------
# 2019/04/14

-------

### 今日完成事宜
- [x]  两天时间了解了Spring
  
  AOP和Ioc有了了解，了解了Spring的Bean机制，了解SpringMVC运行机制。

（1）客户端（浏览器）发送请求，直接请求到 DispatcherServlet。

（2）DispatcherServlet 根据请求信息调用 HandlerMapping，解析请求对应的 Handler。

（3）解析到对应的 Handler（也就是我们平常说的 Controller 控制器）后，开始由 HandlerAdapter 适配器处理。

（4）HandlerAdapter 会根据 Handler 来调用真正的处理器开处理请求，并处理相应的业务逻辑。

（5）处理器处理完业务后，会返回一个 ModelAndView 对象，Model 是返回的数据对象，View 是个逻辑上的 View。

（6）ViewResolver 会根据逻辑 View 查找实际的 View。

（7）DispaterServlet 把返回的 Model 传给 View（视图渲染）。

（8）把 View 返回给请求者（浏览器）

- [x]  计算机网络 
- [x]  Java并发Voletile,原子性，可见性
- [x]  Java多线程的四种方式，run()与start()的区别

-----
### 今日未完成事宜


| 事宜     |预期结果| 当前结果  | 未完成原因   | 
| --------   | -----:  | -----:  | :----:  |
| Mysql | 看完  |了解 | 看了其他内容 |


------
### 明日待办事宜
- [ ] 红黑树算法，MySQL内容

-------
