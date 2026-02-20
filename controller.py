def PID_controller(setpoint, process_variable, vorige_error, Kp, Ki, Kd, integraal, dt):
   error = setpoint - process_variable
   pr = Kp * error  # proportional response
   integraal += error * dt
   ir = Ki * integraal # integral response
   dr = Kd * (error - vorige_error)/dt  # derivative response
   u = pr + ir + dr  # control output
   return u, error


def main():
   setpoint = 20  # voorlopige waarde, gewenste temperatuur ingegeven door gebruiker
   process_variable = 18  # voorlopige waarde, actuele temperatuur bepaald door sensoren
   Kp = 0  # proportional gain, nog te bepalen
   Ki = 0  # integral gain, nog te bepalen
   Kd = 0  # derivative gain, nog te bepalen
   vorige_error = 0  # initiële waarde
   integraal = 0  # initiële waarde
   dt = 1  # voorlopige waarde, tijdstap
   control_output, error = PID_controller(setpoint,process_variable,
vorige_error, Kp, Ki, Kd, integraal, dt)

