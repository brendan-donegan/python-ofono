import dbus


SIM_MANAGER_INTERFACE = 'org.ofono.SimManager'

class SimManager:

    def __init__(self, sim_number=0):
        bus = dbus.SystemBus()
        modem = bus.get_object('org.ofono', '/ril_{}'.format(sim_number)                self._manager = dbus.Interface(modem, SIM_MANAGER_INTERFACE)

    def is_pin_locked():
        """Check if the SIM is locked with a PIN.

        :returns: True if the SIM is locked with a PIN, otherwise False
        """
        locked = self._manager.GetProperties()['LockedPins']
        return 'pin' in locked

    def pin_lock(pin_type, pin):
        """Lock the SIM with a PIN.

        :param pin_type: The type of PIN to lock the SIM with
        :param pin: The PIN with which to lock the SIM
        """
        if not self.is_pin_locked():
            self._manager.LockPin('pin', pin)
