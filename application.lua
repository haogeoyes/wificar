
-----------function------------
    Pin1=1
    Pin2=2
    Pin3=3
    Pin4=4

     function gpioout()
        gpio.mode(Pin1,gpio.OUTPUT)
        gpio.mode(Pin2,gpio.OUTPUT)
        gpio.mode(Pin3,gpio.OUTPUT)
        gpio.mode(Pin4,gpio.OUTPUT)
    end

    function stop()
        gpio.write(Pin1, gpio.LOW)
        gpio.write(Pin2, gpio.LOW)
        gpio.write(Pin3, gpio.LOW)
        gpio.write(Pin4, gpio.LOW)
    end
    function front()
        gpio.write(Pin2, gpio.HIGH)
        gpio.write(Pin4, gpio.HIGH)
        tmr.delay(300000)
        stop()
    end
    function back()
        gpio.write(Pin1, gpio.HIGH)
        gpio.write(Pin3, gpio.HIGH)
        tmr.delay(300000)
        stop()
    end
    
    function left()
        gpio.write(Pin1, gpio.HIGH)
        gpio.write(Pin4, gpio.HIGH)
        tmr.delay(200000)
        stop()
        
    end 
    
    function right()
        gpio.write(Pin2, gpio.HIGH)
        gpio.write(Pin3, gpio.HIGH)
        tmr.delay(200000)
        stop()
        
    end    
    
function resciver_mqtt()
            m = mqtt.Client("1111111110", 1200,"admin","admin")
            
                m:on("message", function(conn, topic, data) 
                  print(topic .. ":" ) 
                  if data ~= nil then
                    print(data)
                    print(type(data))
                  end
                  if data == "front" then
                        gpioout()
                        front()
                  end
                  if data == "back" then
                        gpioout()
                        back()
                  end
                  if data == "left" then
                        gpioout()
                        left()
                  end
                  if data == "right" then
                        gpioout()
                        right()
                  end                                    
                end)
                
                
                --tmr.stop(6)
                --tmr.alarm(6, 5000, 1, function()
                m:connect("192.168.1.111", 1883, 0, function(conn) print("connected") end)
                --m:subscribe("/inode/mychannel",0, function(conn) print("subscribe success") end)

   
end
function loop_sub()
tmr.alarm(1, 1000, 1, 
   function()
        if m == nil then
            resciver_mqtt()
            print("m is nil resciver_mqtt....")
        else
            tmr.stop(1)
            
            print("runnning subscribe....")
            m:subscribe("/inode/mychannel",0, function(conn) print("subscribe success") end)
            
        end
   
   end)
end

function check_loop()
tmr.alarm(3, 10000, 1, 
   function()
        if m == nil then
            a=1
        else
            m:close()
            resciver_mqtt()
            loop_sub()
            
        end
   end)
end
-----------------------main------------------
    Pin1=1
    Pin2=2
    Pin3=3
    Pin4=4
 loop_sub()
 check_loop()
--resciver_mqtt()

--m:subscribe("/inode/mychannel",0, function(conn) print("subscribe success") end)

