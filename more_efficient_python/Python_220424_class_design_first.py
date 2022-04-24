class Kpi:

    def __init__(self, dau, pu, sales):
        self.dau = dau
        self.pu = pu
        self.sales = sales

    def arppu(self):
        return self.sales/self.pu

    def arpu(self):
        return self.sales/self.dau

    def kpi_message(self):
        print('You can calculate kpi_metric using this class')


class KpiAdvance(Kpi):
    def __init__(self, dau, pu, sales, mau, dau_plus_1day):
        Kpi.__init__(self, dau, pu, sales)
        self.mau = mau
        self.dau_plus_1day = dau_plus_1day

    def stickiness(self):
        return self.dau/self.mau

    def retention_1day(self):
        return self.dau_plus_1day/self.dau


kpi_parent = Kpi(1000, 70, 300000)
kpi_parent.__dict__

kpi_parent.arppu()
kpi_parent.arpu()
kpi_parent.kpi_message()

kpi_child = KpiAdvance(1000, 70, 300000, 10000, 300)
kpi_child.__dict__

kpi_child.stickiness()
kpi_child.retention_1day()
kpi_child.kpi_message()

kpi_child.arpu()
kpi_child.arppu()
