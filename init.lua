
wifi.setmode(wifi.STATIONAP)
wifi.sta.config("xiaojidunmogu","dabingjiayiqie")
wifi.sta.connect()
wifi.sta.autoconnect(1)
tmr.alarm(2, 2000, 1, 
   function()
        if wifi.sta.getip() == nil then
            --wifi.sta.connect()
            print("get ip")
        else
            tmr.stop(2)
            gpio.mode(0,gpio.OUTPUT) 
            gpio.write(0, gpio.LOW)
            dofile("application.lua")
            print("runnning run.lua")
            
        end
   
   end)


