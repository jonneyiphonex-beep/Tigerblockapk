package org.tigerblock;

import android.net.VpnService;
import android.content.Intent;
import android.os.ParcelFileDescriptor;

public class BlockVpnService extends VpnService {
    private ParcelFileDescriptor vpnInterface = null;

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Builder builder = new Builder();
        
        // توجيه البيانات لشبكة وهمية معزولة
        builder.addAddress("10.0.0.2", 24);
        builder.addRoute("0.0.0.0", 0);
        
        // حظر تطبيقات محددة عبر الـ Package Name (اختياري)
        try {
            // builder.addDisallowedApplication("com.example.app");
        } catch (Exception e) {
            e.printStackTrace();
        }

        vpnInterface = builder.setSession("TigerBlockVpn")
                              .setBlocking(true)
                              .establish();

        return START_STICKY;
    }

    @Override
    public void onDestroy() {
        if (vpnInterface != null) {
            try { 
                vpnInterface.close(); 
            } catch (Exception ignored) {}
        }
        super.onDestroy();
    }
}